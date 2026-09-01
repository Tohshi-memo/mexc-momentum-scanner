# Decision Report

- generated_at: 2026-09-01T20:01:22.708832+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13267**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13267, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.12% | **-1.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +6.28% | **+1.57%** |
| LIMIT_7PCT | 6/20 | 30.0% | +4.63% | **+1.39%** |
| LIMIT_6PCT | 7/20 | 35.0% | +3.72% | **+1.30%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.26% | **+1.13%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.86% | **+1.86%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.74% | **+1.48%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.96% | **+0.98%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.40% | **+0.77%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.80% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$813.28** / 初期 $100.00 (+713.28%)
- 確定: 4902件 (Win 1493 / Loss 1615 / Flat 1794) / skip 4926件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $813.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.29** / 初期 $100.00 (+75.29%)
- 確定: 2246件 (Win 628 / Loss 540 / Flat 1078) / skip 4432件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0948 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $175.29

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2647件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000204 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-01T20:01:11.554398+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=77296.8
- Funnel: target 1036 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +15.83% | $1,120,769.11 |
| MAGMA/USDT:USDT | +14.40% | $2,135,877.76 |
| USELESS/USDT:USDT | +12.33% | $35,053,287.80 |
| FILECOIN/USDT:USDT | +11.35% | $15,509,009.69 |
| ACE/USDT:USDT | +10.75% | $6,536,996.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FONE/USDT:USDT | below_1h_threshold | +1.38% | +1.36% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +1.31% | +1.29% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +0.88% | +0.86% |
| ONG/USDT:USDT | below_1h_threshold | +0.74% | +0.72% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +0.73% | +0.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
