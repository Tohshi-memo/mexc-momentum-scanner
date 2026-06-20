# Decision Report

- generated_at: 2026-06-20T15:22:00.657578+00:00
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

- 更新: 2026-06-20T15:21:56.284548+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=64160.0
- Funnel: target 796 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +99.68% | $47,558,034.32 |
| BICO/USDT:USDT | +55.99% | $32,896,197.35 |
| BEL/USDT:USDT | +39.21% | $2,645,603.84 |
| RE/USDT:USDT | +38.19% | $79,415,098.30 |
| ALICE/USDT:USDT | +33.33% | $1,033,829.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALICE/USDT:USDT | below_relative_strength | +5.25% | +4.89% |
| RE/USDT:USDT | below_1h_threshold | +3.49% | +3.13% |
| AERO/USDT:USDT | below_1h_threshold | +3.33% | +2.96% |
| CLO/USDT:USDT | below_1h_threshold | +2.92% | +2.56% |
| BICO/USDT:USDT | below_1h_threshold | +2.46% | +2.10% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
