# Decision Report

- generated_at: 2026-09-02T06:16:26.289617+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13313**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13313, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.43% | **-1.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +3.86% | **+1.35%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.86% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +6.31% | **+1.89%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +6.99% | **+1.75%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.61% | **+1.44%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.75% | **+1.14%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +4.37% | **+1.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 197件 (TP 73 / SL 119 / EXP 5)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$832.89** / 初期 $100.00 (+732.89%)
- 確定: 4940件 (Win 1503 / Loss 1625 / Flat 1812) / skip 4934件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $832.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.81** / 初期 $100.00 (+74.81%)
- 確定: 2292件 (Win 637 / Loss 549 / Flat 1106) / skip 4432件
- 成長率目線: 平均log +0.000244 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1117 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $174.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2696件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000317 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-02T06:16:11.785300+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=77580.2
- Funnel: target 1041 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +57.68% | $1,543,632.95 |
| MAGMA/USDT:USDT | +34.38% | $5,688,235.98 |
| CASHCAT/USDT:USDT | +26.34% | $1,475,125.64 |
| BONER/USDT:USDT | +22.31% | $2,636,374.61 |
| UAI/USDT:USDT | +22.00% | $20,892,095.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +2.90% | +2.95% |
| BTW/USDT:USDT | below_1h_threshold | +0.95% | +1.00% |
| ARB/USDT:USDT | below_1h_threshold | +0.84% | +0.89% |
| AKE/USDT:USDT | below_1h_threshold | +0.77% | +0.81% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +0.55% | +0.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
