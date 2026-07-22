# Decision Report

- generated_at: 2026-07-22T16:01:28.746036+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9293**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9293, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 13/20 | 65.0% | +1.22% | **+0.79%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.58% | **+0.52%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.68% | **+0.51%** |
| LIMIT_BB3S | 4/15 | 26.7% | +1.25% | **+0.33%** |
| LIMIT_FIB1272 | 14/20 | 70.0% | +0.40% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.51% | **+0.45%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.74% | **+0.18%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.14% | **-0.01%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.11% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$105.90** / 初期 $100.00 (+5.90%)
- 確定トレード: 132件 (TP 45 / SL 82 / EXP 5)
- 最新: PROM/USDT:USDT TP_HIT PnL +8.00% 残高後 $105.90
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$429.20** / 初期 $100.00 (+329.20%)
- 確定: 3288件 (Win 1038 / Loss 1058 / Flat 1192) / skip 2566件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $429.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1544件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0617 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.55** / 初期 $100.00 (+1.55%)
- 確定: 425件 (Win 142 / Loss 176 / Flat 107) / pending 3件 / skip 346件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000144 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.55

## 6. Latest Market Context

- 更新: 2026-07-22T16:01:20.709012+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=65994.8
- Funnel: target 890 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +1.12% | $3,845,566.37 |
| BEAT/USDT:USDT | +1.11% | $13,524,877.17 |
| RAVE/USDT:USDT | +0.75% | $1,285,864.85 |
| ZHIPUSTOCK/USDT:USDT | +0.63% | $2,337,296.68 |
| ERA/USDT:USDT | +0.47% | $8,215,483.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NVDL/USDT:USDT | below_1h_threshold | +3.75% | +3.78% |
| SOXL/USDT:USDT | below_1h_threshold | +2.55% | +2.58% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.53% | +2.56% |
| ALABSTOCK/USDT:USDT | below_1h_threshold | +1.95% | +1.98% |
| NVIDIA/USDT:USDT | below_1h_threshold | +1.93% | +1.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
