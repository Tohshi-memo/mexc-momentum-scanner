# Decision Report

- generated_at: 2026-11-21T00:31:25.515622+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19272**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19272, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.96% | **-0.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +3.52% | **+1.06%** |
| LIMIT_9PCT | 4/20 | 20.0% | +3.84% | **+0.77%** |
| LIMIT_10PCT | 4/20 | 20.0% | +3.84% | **+0.77%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.58% | **+0.52%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.76% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.62% | **+1.31%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +4.37% | **+1.09%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.91% | **+1.05%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.99% | **+0.99%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.28% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,675.43** / 初期 $100.00 (+1575.43%)
- 確定: 7419件 (Win 2133 / Loss 2393 / Flat 2893) / skip 8414件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAD/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,675.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$439.41** / 初期 $100.00 (+339.41%)
- 確定: 5087件 (Win 1354 / Loss 1088 / Flat 2645) / skip 7596件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0104 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UVXY/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $439.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7434件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000097 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T00:31:11.959705+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=59050.8
- Funnel: target 1086 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +21.50% | $26,275,491.02 |
| PIEVERSE/USDT:USDT | +16.39% | $4,170,992.34 |
| MMT/USDT:USDT | +10.59% | $3,843,274.27 |
| BLESS/USDT:USDT | +10.17% | $21,698,655.78 |
| UVXY/USDT:USDT | +7.09% | $6,685,862.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BARD/USDT:USDT | below_1h_threshold | +1.91% | +1.68% |
| EVAA/USDT:USDT | below_1h_threshold | +1.86% | +1.63% |
| BTW/USDT:USDT | below_1h_threshold | +1.65% | +1.42% |
| BLESS/USDT:USDT | below_1h_threshold | +1.52% | +1.29% |
| SOXS/USDT:USDT | below_1h_threshold | +1.44% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
