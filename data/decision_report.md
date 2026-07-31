# Decision Report

- generated_at: 2026-07-31T08:41:16.155329+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9979**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.78% / filled 20/20。**
- 全期間 MARKET基準: n=9979, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.78% | **+1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_BB3S | 4/8 | 50.0% | +2.48% | **+1.24%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.37% | **+1.10%** |
| LIMIT_7PCT | 2/20 | 10.0% | +4.76% | **+0.48%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.47% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 9/11 | 81.8% | +0.39% | **+0.32%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +1.65% | **+0.25%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.23% | **+0.25%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.16% | **-0.06%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -1.26% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$554.34** / 初期 $100.00 (+454.34%)
- 確定: 3570件 (Win 1141 / Loss 1165 / Flat 1264) / skip 2970件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $554.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.30** / 初期 $100.00 (+42.30%)
- 確定: 1272件 (Win 359 / Loss 294 / Flat 619) / skip 2118件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1305 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $142.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.27** / 初期 $100.00 (+10.27%)
- 確定: 815件 (Win 264 / Loss 325 / Flat 226) / pending 2件 / skip 634件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000259 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $110.27

## 6. Latest Market Context

- 更新: 2026-07-31T08:41:07.609250+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=63832.5
- Funnel: target 921 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +61.27% | $11,249,551.26 |
| GIGGLE/USDT:USDT | +37.97% | $5,458,182.42 |
| MMT/USDT:USDT | +35.22% | $12,547,874.25 |
| AXTISTOCK/USDT:USDT | +30.29% | $4,720,680.70 |
| BULLA/USDT:USDT | +23.25% | $1,377,257.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROBO/USDT:USDT | below_1h_threshold | +3.39% | +3.51% |
| SOXL/USDT:USDT | below_1h_threshold | +2.93% | +3.05% |
| KORU/USDT:USDT | below_1h_threshold | +2.93% | +3.05% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +2.79% | +2.91% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.50% | +2.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
