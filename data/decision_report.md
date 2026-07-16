# Decision Report

- generated_at: 2026-07-16T09:06:15.134514+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8793**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.73% / filled 20/20。**
- 全期間 MARKET基準: n=8793, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.42% | **+1.28%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.42% | **+1.13%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.47% | **+1.03%** |
| LIMIT_BB3S | 6/11 | 54.5% | +1.72% | **+0.94%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.04% | **+0.51%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.82% | **+0.45%** |
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +0.27% | **+0.23%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.55% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$107.41** / 初期 $100.00 (+7.41%)
- 確定トレード: 103件 (TP 38 / SL 63 / EXP 2)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$335.57** / 初期 $100.00 (+235.57%)
- 確定: 2908件 (Win 906 / Loss 945 / Flat 1057) / skip 2446件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $335.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.89** / 初期 $100.00 (+6.89%)
- 確定: 755件 (Win 171 / Loss 169 / Flat 415) / skip 1449件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0070 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RAVE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.65** / 初期 $100.00 (-1.35%)
- 確定: 66件 (Win 20 / Loss 42 / Flat 4) / pending 1件 / skip 198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000611 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAVE/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.65

## 6. Latest Market Context

- 更新: 2026-07-16T09:06:08.848081+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64131.7
- Funnel: target 875 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CAP/USDT:USDT | +18.21% | $2,814,978.05 |
| ROAM/USDT:USDT | +17.81% | $5,801,649.41 |
| AKE/USDT:USDT | +11.87% | $44,092,089.86 |
| ONDO/USDT:USDT | +10.80% | $70,254,024.62 |
| LDO/USDT:USDT | +10.02% | $10,751,283.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROAM/USDT:USDT | below_1h_threshold | +4.96% | +4.90% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +1.54% | +1.48% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +0.92% | +0.87% |
| AKE/USDT:USDT | below_1h_threshold | +0.91% | +0.85% |
| METASTOCK/USDT:USDT | below_1h_threshold | +0.90% | +0.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
