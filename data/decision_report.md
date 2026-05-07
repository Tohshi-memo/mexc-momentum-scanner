# Decision Report

- generated_at: 2026-05-07T02:42:36.198863+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3534**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3534, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.47% | **-1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +4.23% | **+1.06%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.02% | **+0.76%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.26% | **+0.57%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.78% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.82% | **+2.26%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.17% | **+1.95%** |
| MARKET_LONG | 20/20 | 100.0% | +1.83% | **+1.83%** |
| ASK_LONG | 20/20 | 100.0% | +1.82% | **+1.82%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.19% | **+1.75%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定: 29件 (Win 10 / Loss 11 / Flat 8) / skip 66件
- 成長率目線: 平均log +0.000899 / 幾何平均 +0.090% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $102.64

## 4. Latest Market Context

- 更新: 2026-05-07T02:42:33.345910+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=80922.3
- Funnel: target 770 → liquid 188 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +166.86% | $1,115,934.04 |
| DOGS/USDT:USDT | +67.77% | $7,693,225.71 |
| PENGUIN/USDT:USDT | +31.11% | $1,140,540.46 |
| FHE/USDT:USDT | +28.10% | $16,140,545.43 |
| LAB/USDT:USDT | +15.10% | $259,098,115.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.73% | +4.97% |
| DOGS/USDT:USDT | below_1h_threshold | +3.81% | +4.05% |
| NOT/USDT:USDT | below_1h_threshold | +3.27% | +3.51% |
| LAB/USDT:USDT | below_1h_threshold | +2.62% | +2.86% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.58% | +2.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
