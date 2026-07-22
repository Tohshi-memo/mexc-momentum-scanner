# Decision Report

- generated_at: 2026-07-22T05:56:17.667663+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9256**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9256, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.43% | **-1.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.71% | **+0.37%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.42% | **+2.06%** |
| MARKET_LONG | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.44% | **+0.72%** |
| LIMIT_FIB1272_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$425.15** / 初期 $100.00 (+325.15%)
- 確定: 3254件 (Win 1024 / Loss 1040 / Flat 1190) / skip 2563件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $425.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1508件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1682 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.55** / 初期 $100.00 (+2.55%)
- 確定: 397件 (Win 137 / Loss 162 / Flat 98) / pending 3件 / skip 326件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000390 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SMCISTOCK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $102.55

## 6. Latest Market Context

- 更新: 2026-07-22T05:56:10.892869+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.61% price=65944.5
- Funnel: target 885 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +34.23% | $4,267,064.06 |
| LAB/USDT:USDT | +33.18% | $11,238,840.88 |
| SMCISTOCK/USDT:USDT | +18.83% | $4,063,696.33 |
| RE/USDT:USDT | +15.58% | $2,503,050.73 |
| BNCSTOCK/USDT:USDT | +12.83% | $2,858,012.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OPENAI/USDT:USDT | below_1h_threshold | +3.48% | +4.09% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +3.14% | +3.75% |
| AKE/USDT:USDT | below_1h_threshold | +2.92% | +3.53% |
| BILL/USDT:USDT | below_1h_threshold | +2.47% | +3.08% |
| JTO/USDT:USDT | below_1h_threshold | +1.20% | +1.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
