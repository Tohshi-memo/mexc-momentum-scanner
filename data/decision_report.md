# Decision Report

- generated_at: 2026-05-31T21:59:15.473677+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5228**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5228, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.92% | **-1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.26% | **+0.57%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_5PCT | 12/20 | 60.0% | +0.71% | **+0.43%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.95% | **+2.17%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.53% | **+1.52%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.98% | **+1.49%** |
| ASK_LONG | 20/20 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.64% | **+1.32%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.81** / 初期 $100.00 (+31.81%)
- 確定: 863件 (Win 200 / Loss 256 / Flat 407) / skip 926件
- 成長率目線: 平均log +0.000320 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $131.81

## 4. Latest Market Context

- 更新: 2026-05-31T21:59:12.222002+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=73840.0
- Funnel: target 773 → liquid 129 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.5 >= 65=1, 4h RSI 92.0 >= 65=1, 4h RSI 86.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +65.64% | $13,194,643.52 |
| STG/USDT:USDT | +47.81% | $18,384,163.94 |
| HOME/USDT:USDT | +16.28% | $2,944,207.14 |
| ZORA/USDT:USDT | +13.75% | $1,535,367.57 |
| BIANRENSHENG/USDT:USDT | +12.25% | $3,156,621.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +3.93% | +3.76% |
| LAB/USDT:USDT | below_1h_threshold | +3.88% | +3.71% |
| PLAY/USDT:USDT | below_1h_threshold | +3.85% | +3.67% |
| WLD/USDT:USDT | below_1h_threshold | +3.72% | +3.55% |
| MEME/USDT:USDT | below_1h_threshold | +3.51% | +3.33% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
