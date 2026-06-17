# Decision Report

- generated_at: 2026-06-17T12:17:41.195987+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6931**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6931, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.31% | **-0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.44% | **+0.35%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/12 | 58.3% | +2.80% | **+1.64%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.95% | **+0.88%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.33% | **+0.26%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.77** / 初期 $100.00 (+97.77%)
- 確定: 1803件 (Win 490 / Loss 567 / Flat 746) / skip 1689件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTER/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $197.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.55** / 初期 $100.00 (+1.55%)
- 確定: 204件 (Win 48 / Loss 44 / Flat 112) / skip 138件
- 成長率目線: 平均log +0.000075 / 幾何平均 +0.008% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1162 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ASTER/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $101.55

## 5. Latest Market Context

- 更新: 2026-06-17T12:17:35.737529+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64799.5
- Funnel: target 786 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +67.69% | $9,314,012.55 |
| AGT/USDT:USDT | +53.77% | $1,157,691.74 |
| HIGH/USDT:USDT | +31.39% | $3,388,734.77 |
| BP/USDT:USDT | +23.93% | $1,046,254.86 |
| ID/USDT:USDT | +22.45% | $1,553,946.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +4.58% | +4.55% |
| BLESS/USDT:USDT | below_1h_threshold | +3.34% | +3.30% |
| GRASS/USDT:USDT | below_1h_threshold | +3.27% | +3.23% |
| BP/USDT:USDT | below_1h_threshold | +2.57% | +2.53% |
| SIREN/USDT:USDT | below_1h_threshold | +2.30% | +2.26% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
