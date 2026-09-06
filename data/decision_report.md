# Decision Report

- generated_at: 2026-09-06T20:31:30.983531+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13832**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.74% / filled 20/20。**
- 全期間 MARKET基準: n=13832, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.74% | **+0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.93% | **+0.60%** |
| LIMIT_BB3S | 3/18 | 16.7% | +3.58% | **+0.60%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.57% | **+0.54%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.35% | **+0.34%** |
| MARKET_LONG | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | -0.94% | **-0.24%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | -1.93% | **-0.29%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -1.00% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$837.19** / 初期 $100.00 (+737.19%)
- 確定: 5127件 (Win 1538 / Loss 1680 / Flat 1909) / skip 5266件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $837.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2570件 (Win 717 / Loss 618 / Flat 1235) / skip 4673件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.64** / 初期 $100.00 (+18.64%)
- 確定: 2437件 (Win 724 / Loss 931 / Flat 782) / pending 6件 / skip 2865件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000037 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.64

## 6. Latest Market Context

- 更新: 2026-09-06T20:31:14.308378+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=79893.4
- Funnel: target 1059 → liquid 126 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +106.38% | $1,484,350.78 |
| MAGMA/USDT:USDT | +8.77% | $2,175,980.18 |
| TAO/USDT:USDT | +8.25% | $67,195,220.97 |
| BASECAT/USDT:USDT | +7.16% | $1,990,888.09 |
| CRV/USDT:USDT | +6.65% | $4,443,182.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XAN/USDT:USDT | below_1h_threshold | +2.74% | +2.63% |
| PONS/USDT:USDT | below_1h_threshold | +2.39% | +2.27% |
| CRV/USDT:USDT | below_1h_threshold | +2.22% | +2.10% |
| TIA/USDT:USDT | below_1h_threshold | +2.20% | +2.09% |
| FET/USDT:USDT | below_1h_threshold | +2.20% | +2.09% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
