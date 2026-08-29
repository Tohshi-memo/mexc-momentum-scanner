# Decision Report

- generated_at: 2026-08-29T11:31:18.412434+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12932**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=12932, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.07% | **+0.85%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$722.11** / 初期 $100.00 (+622.11%)
- 確定: 4702件 (Win 1424 / Loss 1545 / Flat 1733) / skip 4791件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $722.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$159.84** / 初期 $100.00 (+59.84%)
- 確定: 2016件 (Win 551 / Loss 487 / Flat 978) / skip 4327件
- 成長率目線: 平均log +0.000233 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0631 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $159.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.47** / 初期 $100.00 (+16.47%)
- 確定: 2027件 (Win 596 / Loss 785 / Flat 646) / pending 2件 / skip 2372件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000399 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HNT/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $116.47

## 6. Latest Market Context

- 更新: 2026-08-29T11:31:07.011818+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=77662.1
- Funnel: target 1023 → liquid 140 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +93.53% | $1,848,003.15 |
| HNT/USDT:USDT | +83.26% | $7,773,153.59 |
| 4/USDT:USDT | +44.60% | $2,131,016.63 |
| LONGXIA/USDT:USDT | +19.07% | $2,079,530.16 |
| O/USDT:USDT | +18.61% | $1,452,670.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +3.82% | +3.75% |
| ONG/USDT:USDT | below_1h_threshold | +3.28% | +3.20% |
| BEAT/USDT:USDT | below_1h_threshold | +2.54% | +2.46% |
| NIL/USDT:USDT | below_1h_threshold | +2.49% | +2.42% |
| VELVET/USDT:USDT | below_1h_threshold | +2.26% | +2.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
