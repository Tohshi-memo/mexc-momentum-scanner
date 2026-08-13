# Decision Report

- generated_at: 2026-08-13T00:36:21.893043+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11409**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11409, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 2/18 | 11.1% | +8.00% | **+0.89%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.17% | **+0.35%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.40% | **+1.56%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.57% | **+0.86%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.26% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.08** / 初期 $100.00 (+506.08%)
- 確定: 3949件 (Win 1232 / Loss 1291 / Flat 1426) / skip 4021件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COTI/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $606.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$147.41** / 初期 $100.00 (+47.41%)
- 確定: 1598件 (Win 450 / Loss 374 / Flat 774) / skip 3222件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0827 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $147.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.00** / 初期 $100.00 (+15.00%)
- 確定: 1417件 (Win 416 / Loss 535 / Flat 466) / pending 3件 / skip 1459件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000139 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $115.00

## 6. Latest Market Context

- 更新: 2026-08-13T00:36:15.588310+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=63565.9
- Funnel: target 972 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +43.61% | $12,084,421.87 |
| COTI/USDT:USDT | +32.91% | $7,227,492.07 |
| BTW/USDT:USDT | +15.05% | $21,909,628.29 |
| CASHCAT/USDT:USDT | +11.14% | $1,008,433.11 |
| VELVET/USDT:USDT | +10.77% | $20,680,233.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRVT/USDT:USDT | below_1h_threshold | +3.53% | +3.36% |
| JTO/USDT:USDT | below_1h_threshold | +3.17% | +2.99% |
| VELVET/USDT:USDT | below_1h_threshold | +2.29% | +2.12% |
| LIT/USDT:USDT | below_1h_threshold | +2.02% | +1.85% |
| COTI/USDT:USDT | below_1h_threshold | +1.95% | +1.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
