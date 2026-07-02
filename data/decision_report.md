# Decision Report

- generated_at: 2026-07-02T06:36:06.731670+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8051**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=8051, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| ASK | 20/20 | 100.0% | +2.59% | **+2.59%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +0.83% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +2.10% | **+0.73%** |
| LIMIT_9PCT_LONG | 9/20 | 45.0% | +0.17% | **+0.07%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | -0.37% | **-0.09%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.73% | **-0.40%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | -0.60% | **-0.48%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2168件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 545件 (Win 136 / Loss 131 / Flat 278) / skip 917件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T06:36:01.673848+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=60587.2
- Funnel: target 830 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +159.68% | $84,723,127.03 |
| BIRB/USDT:USDT | +77.61% | $4,047,593.48 |
| RIF/USDT:USDT | +39.53% | $5,444,656.01 |
| TLM/USDT:USDT | +28.57% | $8,082,480.34 |
| LIT/USDT:USDT | +17.75% | $11,163,462.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIRB/USDT:USDT | below_1h_threshold | +4.85% | +4.68% |
| SYN/USDT:USDT | below_1h_threshold | +2.50% | +2.32% |
| RIF/USDT:USDT | below_1h_threshold | +2.14% | +1.96% |
| SLX/USDT:USDT | below_1h_threshold | +1.41% | +1.23% |
| BEAT/USDT:USDT | below_1h_threshold | +0.95% | +0.77% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
