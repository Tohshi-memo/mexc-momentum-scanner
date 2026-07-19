# Decision Report

- generated_at: 2026-07-19T02:51:12.197601+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8995**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8995, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +2.97% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.91% | **+2.47%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.59% | **+2.33%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.94% | **+1.18%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.49% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$370.59** / 初期 $100.00 (+270.59%)
- 確定: 3058件 (Win 951 / Loss 975 / Flat 1132) / skip 2498件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $370.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$122.90** / 初期 $100.00 (+22.90%)
- 確定: 956件 (Win 241 / Loss 194 / Flat 521) / skip 1450件
- 成長率目線: 平均log +0.000216 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2340 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $122.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.47** / 初期 $100.00 (-0.53%)
- 確定: 200件 (Win 64 / Loss 108 / Flat 28) / pending 1件 / skip 264件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000659 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $99.47

## 6. Latest Market Context

- 更新: 2026-07-19T02:51:05.697958+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=64816.0
- Funnel: target 885 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +113.65% | $34,496,636.96 |
| BANK/USDT:USDT | +36.80% | $19,021,255.80 |
| B/USDT:USDT | +21.34% | $34,029,430.49 |
| TLM/USDT:USDT | +17.67% | $3,069,271.75 |
| BILL/USDT:USDT | +16.83% | $3,996,047.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.53% | +4.43% |
| RE/USDT:USDT | below_1h_threshold | +4.50% | +4.39% |
| ZBT/USDT:USDT | below_1h_threshold | +2.42% | +2.32% |
| ZRO/USDT:USDT | below_1h_threshold | +1.66% | +1.56% |
| PI/USDT:USDT | below_1h_threshold | +1.39% | +1.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
