# Decision Report

- generated_at: 2026-08-30T09:51:25.007862+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13046**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.79% / filled 20/20。**
- 全期間 MARKET基準: n=13046, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.79% | **+1.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.79% | **+1.79%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.67% | **+1.59%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.17% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| MARKET_LONG | 20/20 | 100.0% | -0.01% | **-0.01%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$774.74** / 初期 $100.00 (+674.74%)
- 確定: 4807件 (Win 1463 / Loss 1584 / Flat 1760) / skip 4800件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $774.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$172.40** / 初期 $100.00 (+72.40%)
- 確定: 2130件 (Win 593 / Loss 518 / Flat 1019) / skip 4327件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0322 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $172.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.50** / 初期 $100.00 (+16.50%)
- 確定: 2080件 (Win 610 / Loss 809 / Flat 661) / pending 3件 / skip 2436件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000088 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.50

## 6. Latest Market Context

- 更新: 2026-08-30T09:51:14.895595+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=77975.0
- Funnel: target 1023 → liquid 121 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.4 >= 65=1, 4h RSI 79.8 >= 65=1, 4h RSI 80.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +77.69% | $5,011,110.06 |
| HNT/USDT:USDT | +65.88% | $42,767,944.06 |
| PONS/USDT:USDT | +59.63% | $1,804,683.13 |
| ZKC/USDT:USDT | +53.10% | $1,750,104.06 |
| FONE/USDT:USDT | +43.88% | $1,486,802.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +2.42% | +2.52% |
| DEXE/USDT:USDT | below_1h_threshold | +2.19% | +2.28% |
| BEAT/USDT:USDT | below_1h_threshold | +1.25% | +1.34% |
| O/USDT:USDT | below_1h_threshold | +0.64% | +0.73% |
| UAI/USDT:USDT | below_1h_threshold | +0.59% | +0.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
