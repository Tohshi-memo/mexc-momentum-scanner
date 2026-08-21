# Decision Report

- generated_at: 2026-08-21T09:21:26.509409+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12173**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12173, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +6.93% | **+1.39%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +7.19% | **+4.31%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.86% | **+1.77%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.19% | **+1.53%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.07% | **+1.35%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$640.35** / 初期 $100.00 (+540.35%)
- 確定: 4361件 (Win 1337 / Loss 1434 / Flat 1590) / skip 4373件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $640.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1823件 (Win 502 / Loss 429 / Flat 892) / skip 3761件
- 成長率目線: 平均log +0.000237 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0665 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.21** / 初期 $100.00 (+17.21%)
- 確定: 1822件 (Win 540 / Loss 691 / Flat 591) / pending 2件 / skip 1821件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000207 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.21

## 6. Latest Market Context

- 更新: 2026-08-21T09:21:13.699861+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -2.15% price=77571.2
- Funnel: target 1014 → liquid 197 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.1 >= 65=1, 4h RSI 83.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +120.00% | $6,455,453.94 |
| BB/USDT:USDT | +36.57% | $1,693,812.33 |
| ENA/USDT:USDT | +29.88% | $102,229,681.96 |
| PEOPLE/USDT:USDT | +21.31% | $5,478,605.73 |
| HEMI/USDT:USDT | +17.70% | $2,963,804.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GPS/USDT:USDT | below_1h_threshold | +4.68% | +6.83% |
| COINBASE/USDT:USDT | below_1h_threshold | +2.99% | +5.14% |
| RIVER/USDT:USDT | below_1h_threshold | +2.95% | +5.10% |
| CATE/USDT:USDT | below_1h_threshold | +2.57% | +4.71% |
| BTW/USDT:USDT | below_1h_threshold | +1.13% | +3.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
