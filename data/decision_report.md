# Decision Report

- generated_at: 2026-06-01T02:11:18.511717+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5260**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5260, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/9 | 77.8% | +1.31% | **+1.02%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.10% | **+0.49%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.68% | **+0.44%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.42% | **+0.34%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$132.35** / 初期 $100.00 (+32.35%)
- 確定: 892件 (Win 207 / Loss 267 / Flat 418) / skip 929件
- 成長率目線: 平均log +0.000314 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZORA/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $132.35

## 4. Latest Market Context

- 更新: 2026-06-01T02:11:16.044502+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=73495.8
- Funnel: target 777 → liquid 131 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +174.35% | $24,376,961.59 |
| H/USDT:USDT | +71.42% | $18,299,361.29 |
| STG/USDT:USDT | +23.74% | $22,227,144.84 |
| CTR/USDT:USDT | +17.51% | $1,426,739.07 |
| WLD/USDT:USDT | +16.51% | $54,549,238.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +4.81% | +4.48% |
| WLD/USDT:USDT | below_1h_threshold | +3.52% | +3.19% |
| VVV/USDT:USDT | below_1h_threshold | +3.06% | +2.73% |
| FET/USDT:USDT | below_1h_threshold | +2.49% | +2.17% |
| ICP/USDT:USDT | below_1h_threshold | +2.32% | +2.00% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
