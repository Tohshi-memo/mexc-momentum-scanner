# Decision Report

- generated_at: 2026-09-01T20:26:24.518334+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13268**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13268, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.52% | **-0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +6.28% | **+1.57%** |
| LIMIT_7PCT | 6/20 | 30.0% | +4.63% | **+1.39%** |
| LIMIT_6PCT | 6/20 | 30.0% | +4.02% | **+1.21%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.62% | **+1.18%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.46% | **+1.46%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.20% | **+1.02%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.30% | **+0.78%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.42% | **+0.78%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.45% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$813.28** / 初期 $100.00 (+713.28%)
- 確定: 4903件 (Win 1493 / Loss 1615 / Flat 1795) / skip 4926件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $813.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.68** / 初期 $100.00 (+74.68%)
- 確定: 2247件 (Win 628 / Loss 541 / Flat 1078) / skip 4432件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0331 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $174.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2648件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000202 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-01T20:26:13.348597+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=77363.0
- Funnel: target 1036 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +43.80% | $1,316,188.57 |
| MAGMA/USDT:USDT | +17.62% | $2,407,850.65 |
| FONE/USDT:USDT | +13.31% | $1,182,044.55 |
| USELESS/USDT:USDT | +11.62% | $35,773,750.53 |
| FILECOIN/USDT:USDT | +11.33% | $16,867,423.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +1.98% | +1.88% |
| UAI/USDT:USDT | below_1h_threshold | +1.90% | +1.80% |
| ONG/USDT:USDT | below_1h_threshold | +1.83% | +1.73% |
| AR/USDT:USDT | below_1h_threshold | +1.54% | +1.44% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +1.31% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
