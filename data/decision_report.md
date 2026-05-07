# Decision Report

- generated_at: 2026-05-07T12:47:41.038171+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3627**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=3627, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_4PCT | 11/20 | 55.0% | +1.45% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| ASK | 20/20 | 100.0% | +0.75% | **+0.75%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +3.84% | **+1.73%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +2.78% | **+1.67%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.08% | **+0.83%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.21% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.14** / 初期 $100.00 (+7.14%)
- 確定: 121件 (Win 38 / Loss 48 / Flat 35) / skip 67件
- 成長率目線: 平均log +0.000570 / 幾何平均 +0.057% per trade / maxDD +2.62%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $107.14

## 4. Latest Market Context

- 更新: 2026-05-07T12:47:37.858881+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=81012.8
- Funnel: target 771 → liquid 184 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +99.72% | $11,989,195.58 |
| PENGUIN/USDT:USDT | +70.89% | $3,863,724.66 |
| SATO/USDT:USDT | +66.39% | $2,709,105.11 |
| DOGS/USDT:USDT | +52.54% | $16,650,799.35 |
| NIL/USDT:USDT | +36.30% | $3,332,833.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_relative_strength | +5.07% | +4.84% |
| ONDO/USDT:USDT | below_1h_threshold | +4.96% | +4.73% |
| POPCAT/USDT:USDT | below_1h_threshold | +3.41% | +3.18% |
| BRETT/USDT:USDT | below_1h_threshold | +3.31% | +3.09% |
| EVAA/USDT:USDT | below_1h_threshold | +3.20% | +2.98% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
