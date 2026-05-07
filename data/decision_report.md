# Decision Report

- generated_at: 2026-05-07T03:37:36.465262+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3549**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3549, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 7/20 | 35.0% | +3.96% | **+1.39%** |
| LIMIT_9PCT | 6/20 | 30.0% | +3.43% | **+1.03%** |
| LIMIT_7PCT | 9/20 | 45.0% | +2.27% | **+1.02%** |
| LIMIT_6PCT | 10/20 | 50.0% | +1.95% | **+0.98%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.40% | **+2.40%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.40% | **+2.20%** |
| ASK_LONG | 20/20 | 100.0% | +2.19% | **+2.19%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.84% | **+1.71%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.79% | **+1.25%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定: 44件 (Win 14 / Loss 16 / Flat 14) / skip 66件
- 成長率目線: 平均log +0.000845 / 幾何平均 +0.084% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $103.79

## 4. Latest Market Context

- 更新: 2026-05-07T03:37:32.894683+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=80914.6
- Funnel: target 770 → liquid 187 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.9 >= 65=1, 4h RSI 81.6 >= 65=1, 4h RSI 83.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +309.21% | $1,368,831.98 |
| DOGS/USDT:USDT | +87.31% | $9,407,380.65 |
| FHE/USDT:USDT | +35.62% | $16,398,620.49 |
| PENGUIN/USDT:USDT | +28.95% | $1,190,289.45 |
| TONCOIN/USDT:USDT | +18.13% | $263,601,505.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +2.38% | +2.57% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.51% | +1.71% |
| STX/USDT:USDT | below_1h_threshold | +1.48% | +1.68% |
| FILECOIN/USDT:USDT | below_1h_threshold | +1.41% | +1.61% |
| FHE/USDT:USDT | below_1h_threshold | +1.26% | +1.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
