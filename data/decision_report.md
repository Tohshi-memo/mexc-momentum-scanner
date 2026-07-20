# Decision Report

- generated_at: 2026-07-20T01:36:17.709303+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9073**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=9073, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_BB3S | 2/18 | 11.1% | +8.00% | **+0.89%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.81% | **+0.73%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.20% | **+0.66%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| MARKET_LONG | 20/20 | 100.0% | +0.17% | **+0.17%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.30% | **+0.04%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$109.69** / 初期 $100.00 (+9.69%)
- 確定トレード: 119件 (TP 43 / SL 71 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -3.31% 残高後 $109.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$398.27** / 初期 $100.00 (+298.27%)
- 確定: 3135件 (Win 984 / Loss 1001 / Flat 1150) / skip 2499件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $398.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$125.74** / 初期 $100.00 (+25.74%)
- 確定: 1034件 (Win 266 / Loss 218 / Flat 550) / skip 1450件
- 成長率目線: 平均log +0.000222 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0914 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $125.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.90** / 初期 $100.00 (+0.90%)
- 確定: 272件 (Win 94 / Loss 131 / Flat 47) / pending 3件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000206 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $100.90

## 6. Latest Market Context

- 更新: 2026-07-20T01:36:10.535979+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.49% price=64843.9
- Funnel: target 885 → liquid 131 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +48.45% | $2,564,818.08 |
| BANK/USDT:USDT | +44.95% | $86,109,024.12 |
| PUMPFUN/USDT:USDT | +20.10% | $16,193,830.89 |
| PROM/USDT:USDT | +16.69% | $2,044,991.44 |
| AKE/USDT:USDT | +16.16% | $31,997,491.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +4.72% | +4.23% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +2.24% | +1.75% |
| JTO/USDT:USDT | below_1h_threshold | +1.99% | +1.50% |
| PROM/USDT:USDT | below_1h_threshold | +1.97% | +1.48% |
| USELESS/USDT:USDT | below_1h_threshold | +1.94% | +1.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
