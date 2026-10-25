# Decision Report

- generated_at: 2026-10-25T21:01:16.764978+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17436**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17436, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.06% | **+0.06%** |
| LIMIT_ATR | 5/20 | 25.0% | -0.12% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.87% | **+1.78%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +4.99% | **+1.75%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.93% | **+1.54%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,587.10** / 初期 $100.00 (+1487.10%)
- 確定: 6689件 (Win 1948 / Loss 2132 / Flat 2609) / skip 7308件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KIMCHI/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,587.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$320.92** / 初期 $100.00 (+220.92%)
- 確定: 3979件 (Win 1106 / Loss 936 / Flat 1937) / skip 6868件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1897 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KIMCHI/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $320.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5598件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000554 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T21:01:06.865185+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=80444.5
- Funnel: target 1070 → liquid 117 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMCHI/USDT:USDT | +78.46% | $1,196,735.04 |
| APR/USDT:USDT | +6.60% | $13,098,033.41 |
| AGT/USDT:USDT | +4.07% | $3,435,381.15 |
| PYTH/USDT:USDT | +3.39% | $2,183,351.45 |
| INJ/USDT:USDT | +3.18% | $17,174,603.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +0.47% | +0.49% |
| APR/USDT:USDT | below_1h_threshold | +0.23% | +0.24% |
| SOXL/USDT:USDT | below_1h_threshold | +0.13% | +0.14% |
| TAG/USDT:USDT | below_1h_threshold | +0.12% | +0.14% |
| SNXX/USDT:USDT | below_1h_threshold | +0.12% | +0.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
