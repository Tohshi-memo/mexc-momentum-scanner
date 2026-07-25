# Decision Report

- generated_at: 2026-07-25T22:01:20.020512+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9542**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9542, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.40% | **+0.49%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.42% | **+1.21%** |
| MARKET_LONG | 20/20 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.98% | **+0.64%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.01% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$455.98** / 初期 $100.00 (+355.98%)
- 確定: 3370件 (Win 1070 / Loss 1092 / Flat 1208) / skip 2733件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B2/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $455.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.61** / 初期 $100.00 (+37.61%)
- 確定: 1195件 (Win 330 / Loss 262 / Flat 603) / skip 1758件
- 成長率目線: 平均log +0.000267 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1537 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: B2/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 586件 (Win 198 / Loss 225 / Flat 163) / pending 4件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000463 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B2/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $107.86

## 6. Latest Market Context

- 更新: 2026-07-25T22:01:11.953120+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64322.9
- Funnel: target 898 → liquid 120 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +19.10% | $25,574,614.14 |
| EUL/USDT:USDT | +17.83% | $18,436,927.58 |
| VELVET/USDT:USDT | +12.10% | $7,947,803.30 |
| ALLO/USDT:USDT | +11.84% | $17,695,350.91 |
| BANK/USDT:USDT | +10.68% | $89,432,058.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +0.58% | +0.57% |
| VELVET/USDT:USDT | below_1h_threshold | +0.50% | +0.49% |
| SHIB/USDT:USDT | below_1h_threshold | +0.39% | +0.38% |
| ZAMA/USDT:USDT | below_1h_threshold | +0.27% | +0.26% |
| WIF/USDT:USDT | below_1h_threshold | +0.25% | +0.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
