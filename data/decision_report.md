# Decision Report

- generated_at: 2026-08-21T18:46:27.742840+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12239**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=12239, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.07% | **+0.91%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.21% | **+0.91%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.97% | **+0.87%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +3.61% | **+1.99%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +2.76% | **+1.79%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +2.05% | **+1.64%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +1.53% | **+1.30%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.10% | **+1.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$643.52** / 初期 $100.00 (+543.52%)
- 確定: 4367件 (Win 1338 / Loss 1435 / Flat 1594) / skip 4433件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $643.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.01** / 初期 $100.00 (+56.01%)
- 確定: 1849件 (Win 512 / Loss 440 / Flat 897) / skip 3801件
- 成長率目線: 平均log +0.000241 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0636 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $156.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1893件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000159 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T18:46:17.156789+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.00% price=76608.2
- Funnel: target 1018 → liquid 212 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +41.25% | $11,223,317.72 |
| JIMOTHY/USDT:USDT | +24.03% | $1,167,021.37 |
| BEAT/USDT:USDT | +11.34% | $56,216,046.17 |
| BICO/USDT:USDT | +9.76% | $3,157,171.31 |
| GPS/USDT:USDT | +8.49% | $3,870,968.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GPS/USDT:USDT | below_1h_threshold | +2.83% | +3.83% |
| BANK/USDT:USDT | below_1h_threshold | +2.41% | +3.41% |
| PROM/USDT:USDT | below_1h_threshold | +2.33% | +3.33% |
| LIT/USDT:USDT | below_1h_threshold | +1.84% | +2.84% |
| ONG/USDT:USDT | below_1h_threshold | +1.76% | +2.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
