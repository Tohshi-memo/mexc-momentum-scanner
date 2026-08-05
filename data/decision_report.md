# Decision Report

- generated_at: 2026-08-05T10:26:23.560139+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10392**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=10392, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +1.28% | **+1.09%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.45% | **+0.94%** |
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_BB3S | 6/19 | 31.6% | +1.92% | **+0.61%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.52% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.73% | **+0.86%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.54% | **+0.29%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.42% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$608.35** / 初期 $100.00 (+508.35%)
- 確定: 3768件 (Win 1195 / Loss 1235 / Flat 1338) / skip 3185件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CYS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $608.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.85** / 初期 $100.00 (+43.85%)
- 確定: 1315件 (Win 372 / Loss 309 / Flat 634) / skip 2488件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0899 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $143.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.57** / 初期 $100.00 (+18.57%)
- 確定: 1133件 (Win 364 / Loss 438 / Flat 331) / pending 5件 / skip 727件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000295 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.57

## 6. Latest Market Context

- 更新: 2026-08-05T10:26:14.543592+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=64165.0
- Funnel: target 945 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +84.24% | $37,908,711.61 |
| HFT/USDT:USDT | +73.32% | $3,337,025.74 |
| HEI/USDT:USDT | +65.87% | $20,301,517.28 |
| SKR/USDT:USDT | +28.63% | $1,677,001.60 |
| BICO/USDT:USDT | +27.85% | $16,812,632.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HFT/USDT:USDT | below_1h_threshold | +4.98% | +4.92% |
| SKR/USDT:USDT | below_1h_threshold | +4.66% | +4.60% |
| EVAA/USDT:USDT | below_1h_threshold | +3.64% | +3.58% |
| CAP/USDT:USDT | below_1h_threshold | +1.98% | +1.92% |
| KAITO/USDT:USDT | below_1h_threshold | +1.78% | +1.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
