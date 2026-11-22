# Decision Report

- generated_at: 2026-11-22T10:16:18.989129+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19376**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19376, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 10/18 | 55.6% | +1.43% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +6.26% | **+6.26%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.02% | **+1.11%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.96% | **+1.08%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.38% | **+0.83%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.13% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 284件 (TP 103 / SL 173 / EXP 8)
- 最新: MMT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,818.67** / 初期 $100.00 (+1718.67%)
- 確定: 7486件 (Win 2152 / Loss 2409 / Flat 2925) / skip 8451件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,818.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$455.03** / 初期 $100.00 (+355.03%)
- 確定: 5140件 (Win 1368 / Loss 1105 / Flat 2667) / skip 7647件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0537 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $455.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7536件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000365 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T10:16:04.384677+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=60920.2
- Funnel: target 1086 → liquid 105 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIEVERSE/USDT:USDT | +68.04% | $15,800,492.98 |
| CLAUDIA/USDT:USDT | +52.24% | $2,536,715.06 |
| BTW/USDT:USDT | +15.62% | $5,181,472.31 |
| MMT/USDT:USDT | +12.58% | $1,897,651.21 |
| BLESS/USDT:USDT | +11.73% | $45,059,142.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLAUDIA/USDT:USDT | below_1h_threshold | +2.32% | +2.61% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.29% | +2.59% |
| DCTY/USDT:USDT | below_1h_threshold | +1.97% | +2.27% |
| KORU/USDT:USDT | below_1h_threshold | +1.44% | +1.74% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.24% | +1.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
