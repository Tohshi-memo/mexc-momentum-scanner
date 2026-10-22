# Decision Report

- generated_at: 2026-10-22T09:21:41.005666+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17135**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17135, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.78% | **-1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +6.93% | **+1.39%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_BB3S | 6/17 | 35.3% | +0.78% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.90% | **+1.31%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.29% | **+0.90%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.69% | **+0.85%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.31% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,358.99** / 初期 $100.00 (+1258.99%)
- 確定: 6517件 (Win 1894 / Loss 2076 / Flat 2547) / skip 7179件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PTB/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.24% 残高後 $1,358.99

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.63** / 初期 $100.00 (+177.63%)
- 確定: 3839件 (Win 1055 / Loss 899 / Flat 1885) / skip 6707件
- 成長率目線: 平均log +0.000266 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0685 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PTB/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $277.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5295件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000168 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-22T09:21:22.271905+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=81854.3
- Funnel: target 1090 → liquid 188 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PTB/USDT:USDT | +58.76% | $1,585,767.98 |
| MAGMA/USDT:USDT | +43.33% | $3,732,847.35 |
| AGT/USDT:USDT | +22.86% | $5,160,721.77 |
| SOXS/USDT:USDT | +12.17% | $11,920,603.47 |
| BILL/USDT:USDT | +11.78% | $1,063,479.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +2.93% | +2.88% |
| PARTI/USDT:USDT | below_1h_threshold | +2.52% | +2.47% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.11% | +2.06% |
| VVV/USDT:USDT | below_1h_threshold | +2.03% | +1.98% |
| RIVER/USDT:USDT | below_1h_threshold | +1.31% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
