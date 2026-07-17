# Decision Report

- generated_at: 2026-07-17T21:01:13.017138+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8886**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8886, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_BB3S | 5/19 | 26.3% | +2.55% | **+0.67%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.83% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.33% | **+0.87%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.00% | **+0.55%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.63% | **+0.32%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.39% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$112.93** / 初期 $100.00 (+12.93%)
- 確定トレード: 112件 (TP 43 / SL 65 / EXP 4)
- 最新: BSB/USDT:USDT TP_HIT PnL +8.00% 残高後 $112.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$365.69** / 初期 $100.00 (+265.69%)
- 確定: 3001件 (Win 934 / Loss 953 / Flat 1114) / skip 2446件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $365.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.54** / 初期 $100.00 (+11.54%)
- 確定: 848件 (Win 201 / Loss 173 / Flat 474) / skip 1449件
- 成長率目線: 平均log +0.000129 / 幾何平均 +0.013% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0884 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $111.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.60** / 初期 $100.00 (-0.40%)
- 確定: 146件 (Win 47 / Loss 79 / Flat 20) / pending 3件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000341 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $99.60

## 6. Latest Market Context

- 更新: 2026-07-17T21:01:07.972038+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64102.5
- Funnel: target 885 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +30.31% | $42,449,558.74 |
| ESPORTS/USDT:USDT | +24.16% | $9,066,853.45 |
| XEC/USDT:USDT | +8.06% | $3,157,620.08 |
| VVV/USDT:USDT | +6.12% | $2,421,468.05 |
| CRO/USDT:USDT | +4.76% | $2,210,984.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DODO/USDT:USDT | below_1h_threshold | +0.88% | +0.85% |
| SOXS/USDT:USDT | below_1h_threshold | +0.66% | +0.63% |
| JTO/USDT:USDT | below_1h_threshold | +0.62% | +0.59% |
| AKE/USDT:USDT | below_1h_threshold | +0.49% | +0.46% |
| ZINC/USDT:USDT | below_1h_threshold | +0.44% | +0.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
