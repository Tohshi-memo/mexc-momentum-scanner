# Decision Report

- generated_at: 2026-07-21T05:46:09.605696+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9157**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.60% / filled 20/20。**
- 全期間 MARKET基準: n=9157, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.97% | **+0.59%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.97% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +7.51% | **+2.50%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.83% | **+1.65%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.51% | **+1.21%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.10% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.47% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$108.05** / 初期 $100.00 (+8.05%)
- 確定トレード: 125件 (TP 44 / SL 76 / EXP 5)
- 最新: KIOXIASTOCK/USDT:USDT SL_HIT PnL -3.51% 残高後 $108.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$417.29** / 初期 $100.00 (+317.29%)
- 確定: 3219件 (Win 1010 / Loss 1026 / Flat 1183) / skip 2499件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 1000BONK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $417.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.41** / 初期 $100.00 (+30.41%)
- 確定: 1118件 (Win 296 / Loss 234 / Flat 588) / skip 1450件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0794 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 1000BONK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $130.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 341件 (Win 120 / Loss 152 / Flat 69) / pending 0件 / skip 284件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 1000BONK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.91

## 6. Latest Market Context

- 更新: 2026-07-21T05:46:02.991566+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=65607.1
- Funnel: target 885 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +73.94% | $3,305,304.89 |
| ERA/USDT:USDT | +64.88% | $4,721,525.50 |
| ZHIPUSTOCK/USDT:USDT | +29.35% | $2,245,240.52 |
| LDO/USDT:USDT | +11.20% | $8,666,614.02 |
| ESPORTS/USDT:USDT | +10.55% | $5,502,957.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.98% | +3.81% |
| USELESS/USDT:USDT | below_1h_threshold | +2.82% | +2.65% |
| OPENAI/USDT:USDT | below_1h_threshold | +2.34% | +2.17% |
| ADA/USDT:USDT | below_1h_threshold | +2.32% | +2.15% |
| B/USDT:USDT | below_1h_threshold | +1.75% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
