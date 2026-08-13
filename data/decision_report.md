# Decision Report

- generated_at: 2026-08-13T15:11:25.150938+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11451**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11451, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.78% | **-0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +0.93% | **+0.79%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_ATR | 18/20 | 90.0% | +0.18% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.42% | **+1.14%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.98% | **+1.04%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.05% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$619.18** / 初期 $100.00 (+519.18%)
- 確定: 3969件 (Win 1239 / Loss 1297 / Flat 1433) / skip 4043件
- 成長率目線: 平均log +0.000459 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNXX/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $619.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$152.35** / 初期 $100.00 (+52.35%)
- 確定: 1639件 (Win 469 / Loss 390 / Flat 780) / skip 3223件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1017 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $152.35

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1455件 (Win 429 / Loss 547 / Flat 479) / pending 5件 / skip 1467件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000291 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-13T15:11:15.477310+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63823.0
- Funnel: target 978 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +52.01% | $24,698,405.87 |
| ACU/USDT:USDT | +31.96% | $7,924,603.85 |
| AVNT/USDT:USDT | +26.78% | $2,421,528.71 |
| COTI/USDT:USDT | +26.44% | $11,783,667.72 |
| AVAAI/USDT:USDT | +25.27% | $1,849,900.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SMCISTOCK/USDT:USDT | below_1h_threshold | +4.78% | +4.80% |
| MUU/USDT:USDT | below_1h_threshold | +3.30% | +3.32% |
| CIENSTOCK/USDT:USDT | below_1h_threshold | +3.17% | +3.19% |
| INFQSTOCK/USDT:USDT | below_1h_threshold | +2.79% | +2.81% |
| BR/USDT:USDT | below_1h_threshold | +2.52% | +2.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
