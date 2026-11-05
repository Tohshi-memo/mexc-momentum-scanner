# Decision Report

- generated_at: 2026-11-05T16:46:53.664638+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18189**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.90% / filled 20/20。**
- 全期間 MARKET基準: n=18189, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +5.69% | **+1.42%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +4.55% | **+1.36%** |
| MARKET_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.82% | **+0.62%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.49% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 263件 (TP 96 / SL 159 / EXP 8)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,505.05** / 初期 $100.00 (+1405.05%)
- 確定: 7008件 (Win 2021 / Loss 2243 / Flat 2744) / skip 7742件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,505.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$374.11** / 初期 $100.00 (+274.11%)
- 確定: 4581件 (Win 1231 / Loss 1030 / Flat 2320) / skip 7019件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0049 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $374.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6356件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000379 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-05T16:46:33.982988+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.54% price=76425.9
- Funnel: target 1084 → liquid 188 → pre 50 → checked 50 → surge 5 → strict 4
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +18.56% | $14,545,886.00 |
| SNXX/USDT:USDT | +11.74% | $55,659,089.33 |
| MUU/USDT:USDT | +10.65% | $34,823,022.36 |
| BLESS/USDT:USDT | +9.56% | $2,604,333.67 |
| ARIA/USDT:USDT | +8.18% | $3,471,483.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| Q/USDT:USDT | below_1h_threshold | +4.79% | +4.25% |
| LYN/USDT:USDT | below_1h_threshold | +4.29% | +3.75% |
| XTZ/USDT:USDT | below_1h_threshold | +3.71% | +3.17% |
| CLANKER/USDT:USDT | below_1h_threshold | +3.30% | +2.76% |
| HOT/USDT:USDT | below_1h_threshold | +2.73% | +2.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
