# Decision Report

- generated_at: 2026-09-09T05:06:15.675168+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14033**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.50% / filled 20/20。**
- 全期間 MARKET基準: n=14033, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.50% | **+2.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.50% | **+2.50%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.22% | **+2.00%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.54% | **+1.90%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.83% | **+1.70%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.01% | **+1.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.02% | **+0.02%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -2.80% | **-0.56%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,010.91** / 初期 $100.00 (+910.91%)
- 確定: 5297件 (Win 1590 / Loss 1708 / Flat 1999) / skip 5297件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $1,010.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.99** / 初期 $100.00 (+89.99%)
- 確定: 2636件 (Win 726 / Loss 623 / Flat 1287) / skip 4808件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0372 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $189.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.85** / 初期 $100.00 (+18.85%)
- 確定: 2613件 (Win 764 / Loss 995 / Flat 854) / pending 3件 / skip 2887件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000279 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.85

## 6. Latest Market Context

- 更新: 2026-09-09T05:06:06.419013+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=79102.6
- Funnel: target 1070 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OL/USDT:USDT | +23.89% | $2,090,369.32 |
| WAVES/USDT:USDT | +14.61% | $1,568,332.87 |
| NIULAI/USDT:USDT | +12.92% | $1,221,896.36 |
| CNPY/USDT:USDT | +11.80% | $1,034,476.81 |
| RAY/USDT:USDT | +11.50% | $2,689,456.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +4.70% | +4.74% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.89% | +2.93% |
| BNCSTOCK/USDT:USDT | below_1h_threshold | +2.43% | +2.47% |
| XAN/USDT:USDT | below_1h_threshold | +2.17% | +2.21% |
| HNT/USDT:USDT | below_1h_threshold | +1.77% | +1.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
