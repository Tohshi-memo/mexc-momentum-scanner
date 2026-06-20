# Decision Report

- generated_at: 2026-06-20T14:38:20.948123+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7248**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=7248, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.94% | **+1.74%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.03% | **+0.98%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.76% | **+0.60%** |
| ASK | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.55% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.65% | **+0.26%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.27% | **+0.12%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.22% | **+0.09%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$228.21** / 初期 $100.00 (+128.21%)
- 確定: 1978件 (Win 576 / Loss 644 / Flat 758) / skip 1831件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SLX/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $228.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 349件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T14:38:14.221443+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=63413.3
- Funnel: target 796 → liquid 144 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +104.32% | $44,111,326.34 |
| BICO/USDT:USDT | +50.69% | $32,203,844.87 |
| BEL/USDT:USDT | +40.52% | $2,502,341.01 |
| SLX/USDT:USDT | +34.85% | $1,428,787.58 |
| RE/USDT:USDT | +28.52% | $82,476,673.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +3.67% | +3.60% |
| CLO/USDT:USDT | below_1h_threshold | +2.77% | +2.70% |
| EVAA/USDT:USDT | below_1h_threshold | +2.34% | +2.26% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.27% | +2.20% |
| JUP/USDT:USDT | below_1h_threshold | +2.24% | +2.16% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
