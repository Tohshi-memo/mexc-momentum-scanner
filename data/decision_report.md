# Decision Report

- generated_at: 2026-07-31T07:26:28.069437+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9971**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9971, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.46% | **-0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.44% | **+0.97%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.14% | **+0.92%** |
| LIMIT_10PCT | 2/20 | 10.0% | +7.36% | **+0.74%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.38% | **+0.68%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.83% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.25% | **+1.12%** |
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.88% | **+0.66%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.35% | **+0.19%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.24% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$555.74** / 初期 $100.00 (+455.74%)
- 確定: 3562件 (Win 1138 / Loss 1160 / Flat 1264) / skip 2970件
- 成長率目線: 平均log +0.000482 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $555.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.10** / 初期 $100.00 (+42.10%)
- 確定: 1265件 (Win 356 / Loss 290 / Flat 619) / skip 2117件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1499 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $142.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.37** / 初期 $100.00 (+10.37%)
- 確定: 808件 (Win 262 / Loss 321 / Flat 225) / pending 6件 / skip 634件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000467 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $110.37

## 6. Latest Market Context

- 更新: 2026-07-31T07:26:20.751671+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=63974.4
- Funnel: target 920 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +59.76% | $10,343,198.76 |
| MMT/USDT:USDT | +33.68% | $12,118,143.67 |
| AXTISTOCK/USDT:USDT | +31.22% | $4,546,902.23 |
| GIGGLE/USDT:USDT | +30.03% | $2,376,107.80 |
| BULLA/USDT:USDT | +28.84% | $1,241,196.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KOMA/USDT:USDT | below_1h_threshold | +2.98% | +3.34% |
| US/USDT:USDT | below_1h_threshold | +2.84% | +3.20% |
| CAP/USDT:USDT | below_1h_threshold | +1.87% | +2.24% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.20% | +1.56% |
| BEAT/USDT:USDT | below_1h_threshold | +1.00% | +1.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
