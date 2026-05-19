# Decision Report

- generated_at: 2026-05-19T07:14:11.114717+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4463**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4463, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +1.25% | **+0.87%** |
| ASK | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.41% | **+0.36%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.89% | **+1.61%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.37% | **+0.83%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +1.55% | **+0.78%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.77% | **+0.58%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +2.01% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$96.70** / 初期 $100.00 (-3.30%)
- 確定トレード: 54件 (TP 14 / SL 37 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +5.37% 残高後 $96.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.06** / 初期 $100.00 (+23.06%)
- 確定: 460件 (Win 122 / Loss 158 / Flat 180) / skip 564件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $123.06

## 4. Latest Market Context

- 更新: 2026-05-19T07:14:08.948021+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=77090.0
- Funnel: target 768 → liquid 137 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +28.22% | $8,699,922.51 |
| PLAY/USDT:USDT | +20.27% | $1,748,342.41 |
| EDEN/USDT:USDT | +14.28% | $1,947,824.29 |
| ONDO/USDT:USDT | +13.86% | $52,213,988.91 |
| ONT/USDT:USDT | +10.72% | $1,013,532.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +1.42% | +1.29% |
| HYPE/USDT:USDT | below_1h_threshold | +0.74% | +0.60% |
| ZEN/USDT:USDT | below_1h_threshold | +0.65% | +0.52% |
| STRK/USDT:USDT | below_1h_threshold | +0.53% | +0.40% |
| DASH/USDT:USDT | below_1h_threshold | +0.42% | +0.29% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
