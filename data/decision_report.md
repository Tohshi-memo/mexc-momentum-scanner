# Decision Report

- generated_at: 2026-10-13T04:11:28.247540+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16629**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16629, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/12 | 33.3% | +2.53% | **+0.84%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.06% | **+0.64%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_8PCT | 6/20 | 30.0% | +1.28% | **+0.39%** |
| LIMIT_9PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.38% | **+1.32%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_BB3S_LONG | 3/8 | 37.5% | +3.00% | **+1.13%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,285.29** / 初期 $100.00 (+1185.29%)
- 確定: 6294件 (Win 1845 / Loss 2017 / Flat 2432) / skip 6896件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGIC/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,285.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$271.33** / 初期 $100.00 (+171.33%)
- 確定: 3646件 (Win 1012 / Loss 859 / Flat 1775) / skip 6394件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TIA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $271.33

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4790件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000142 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-13T04:11:16.337167+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=83258.6
- Funnel: target 1089 → liquid 192 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BAT/USDT:USDT | +17.10% | $6,053,249.26 |
| LONGXIA/USDT:USDT | +14.20% | $1,031,587.11 |
| STX/USDT:USDT | +10.04% | $15,234,885.13 |
| SYN/USDT:USDT | +9.00% | $1,157,160.05 |
| RENDER/USDT:USDT | +6.32% | $18,974,383.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAT/USDT:USDT | below_1h_threshold | +2.16% | +2.21% |
| CT/USDT:USDT | below_1h_threshold | +1.93% | +1.97% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +1.79% | +1.83% |
| TIA/USDT:USDT | below_1h_threshold | +1.46% | +1.51% |
| XAI/USDT:USDT | below_1h_threshold | +1.41% | +1.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
