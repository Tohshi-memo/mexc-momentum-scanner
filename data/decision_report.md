# Decision Report

- generated_at: 2026-09-07T01:11:13.632378+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13854**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.39% / filled 20/20。**
- 全期間 MARKET基準: n=13854, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 7/20 | 35.0% | +6.29% | **+2.20%** |
| LIMIT_7PCT | 7/20 | 35.0% | +5.54% | **+1.94%** |
| LIMIT_9PCT | 6/20 | 30.0% | +6.00% | **+1.80%** |
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.59% | **+1.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.42% | **+0.85%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.47% | **+0.59%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.33% | **+0.26%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.25% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$837.19** / 初期 $100.00 (+737.19%)
- 確定: 5128件 (Win 1538 / Loss 1680 / Flat 1910) / skip 5287件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TIA/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $837.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2570件 (Win 717 / Loss 618 / Flat 1235) / skip 4695件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0360 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.04** / 初期 $100.00 (+19.04%)
- 確定: 2448件 (Win 728 / Loss 935 / Flat 785) / pending 0件 / skip 2874件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000242 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TIA/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $119.04

## 6. Latest Market Context

- 更新: 2026-09-07T01:11:03.665322+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=79928.4
- Funnel: target 1059 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +140.79% | $3,760,079.28 |
| METIS/USDT:USDT | +16.83% | $1,007,571.25 |
| TIA/USDT:USDT | +10.63% | $16,536,005.32 |
| MAGMA/USDT:USDT | +9.79% | $2,149,136.95 |
| XAN/USDT:USDT | +8.94% | $1,421,543.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +1.85% | +2.10% |
| BONER/USDT:USDT | below_1h_threshold | +1.56% | +1.80% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.23% | +1.47% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.84% | +1.08% |
| SOXL/USDT:USDT | below_1h_threshold | +0.52% | +0.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
