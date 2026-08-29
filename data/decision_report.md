# Decision Report

- generated_at: 2026-08-29T10:51:27.726150+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12929**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=12929, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.13% | **+0.96%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.30% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$724.03** / 初期 $100.00 (+624.03%)
- 確定: 4699件 (Win 1423 / Loss 1544 / Flat 1732) / skip 4791件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $724.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$159.31** / 初期 $100.00 (+59.31%)
- 確定: 2013件 (Win 550 / Loss 486 / Flat 977) / skip 4327件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0094 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $159.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.48** / 初期 $100.00 (+16.48%)
- 確定: 2024件 (Win 595 / Loss 783 / Flat 646) / pending 3件 / skip 2372件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000355 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $116.48

## 6. Latest Market Context

- 更新: 2026-08-29T10:51:13.961029+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=77692.4
- Funnel: target 1023 → liquid 144 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.0 >= 65=1, 4h RSI 78.6 >= 65=1, 4h RSI 84.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +99.50% | $1,804,867.34 |
| HNT/USDT:USDT | +88.96% | $6,042,055.37 |
| 4/USDT:USDT | +37.09% | $1,851,400.22 |
| O/USDT:USDT | +17.47% | $1,348,630.73 |
| AKE/USDT:USDT | +12.99% | $20,257,085.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +4.70% | +4.61% |
| PROM/USDT:USDT | below_1h_threshold | +4.14% | +4.04% |
| VELVET/USDT:USDT | below_1h_threshold | +2.70% | +2.60% |
| AKE/USDT:USDT | below_1h_threshold | +1.61% | +1.51% |
| ZEC/USDT:USDT | below_1h_threshold | +1.33% | +1.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
