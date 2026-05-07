# Decision Report

- generated_at: 2026-05-07T12:07:30.099332+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3622**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=3622, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.27% | **+1.27%** |
| ASK | 20/20 | 100.0% | +0.78% | **+0.78%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.34% | **+0.27%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.36% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +2.06% | **+1.96%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.92% | **+0.87%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.22% | **+0.79%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.82% | **+0.73%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.92% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.53** / 初期 $100.00 (+6.53%)
- 確定: 116件 (Win 37 / Loss 47 / Flat 32) / skip 67件
- 成長率目線: 平均log +0.000546 / 幾何平均 +0.055% per trade / maxDD +2.62%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.28% 残高後 $106.53

## 4. Latest Market Context

- 更新: 2026-05-07T12:07:26.570643+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=80901.8
- Funnel: target 771 → liquid 182 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +117.44% | $2,339,209.93 |
| B3/USDT:USDT | +96.88% | $11,786,175.53 |
| PENGUIN/USDT:USDT | +76.58% | $3,723,228.13 |
| DOGS/USDT:USDT | +52.39% | $16,251,632.35 |
| NIL/USDT:USDT | +33.94% | $2,985,301.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KSM/USDT:USDT | below_1h_threshold | +2.30% | +2.21% |
| DOGS/USDT:USDT | below_1h_threshold | +2.21% | +2.12% |
| EVAA/USDT:USDT | below_1h_threshold | +1.94% | +1.85% |
| D/USDT:USDT | below_1h_threshold | +1.70% | +1.61% |
| WLFI/USDT:USDT | below_1h_threshold | +1.50% | +1.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
