# Decision Report

- generated_at: 2026-05-31T21:48:25.164011+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5226**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5226, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.92% | **-1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.59% | **+0.88%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_BB3S | 11/20 | 55.0% | +0.39% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.54% | **+1.77%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.98% | **+1.49%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.78% | **+1.11%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.86% | **+1.02%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.28% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.50** / 初期 $100.00 (+30.50%)
- 確定: 861件 (Win 199 / Loss 256 / Flat 406) / skip 926件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $130.50

## 4. Latest Market Context

- 更新: 2026-05-31T21:48:22.596743+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=73849.7
- Funnel: target 773 → liquid 129 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +45.60% | $17,680,201.44 |
| PORTAL/USDT:USDT | +18.78% | $12,344,966.65 |
| HOME/USDT:USDT | +18.69% | $2,904,381.80 |
| BIANRENSHENG/USDT:USDT | +11.87% | $3,136,575.32 |
| ZORA/USDT:USDT | +11.19% | $1,482,010.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +4.79% | +4.60% |
| WLD/USDT:USDT | below_1h_threshold | +4.01% | +3.83% |
| MEME/USDT:USDT | below_1h_threshold | +3.29% | +3.10% |
| MYX/USDT:USDT | below_1h_threshold | +3.25% | +3.06% |
| LAB/USDT:USDT | below_1h_threshold | +3.01% | +2.82% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
