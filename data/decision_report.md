# Decision Report

- generated_at: 2026-09-06T16:16:29.438436+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13824**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.82% / filled 20/20。**
- 全期間 MARKET基準: n=13824, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.82% | **+2.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +3.43% | **+3.09%** |
| MARKET | 20/20 | 100.0% | +2.82% | **+2.82%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.75% | **+1.37%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.29% | **+1.26%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +4.16% | **+1.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.01% | **+0.25%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +0.37% | **+0.13%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.40% | **-0.20%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | -0.87% | **-0.56%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$837.19** / 初期 $100.00 (+737.19%)
- 確定: 5127件 (Win 1538 / Loss 1680 / Flat 1909) / skip 5258件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $837.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.84** / 初期 $100.00 (+88.84%)
- 確定: 2568件 (Win 717 / Loss 617 / Flat 1234) / skip 4667件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0509 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $188.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.85** / 初期 $100.00 (+18.85%)
- 確定: 2435件 (Win 724 / Loss 930 / Flat 781) / pending 3件 / skip 2856件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000142 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.85

## 6. Latest Market Context

- 更新: 2026-09-06T16:16:13.391219+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=79666.0
- Funnel: target 1059 → liquid 126 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +8.57% | $2,202,327.03 |
| 4/USDT:USDT | +5.93% | $13,788,450.94 |
| USELESS/USDT:USDT | +3.86% | $17,202,699.27 |
| PONS/USDT:USDT | +2.50% | $11,192,697.81 |
| MARSCOIN/USDT:USDT | +2.31% | $4,948,964.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +3.99% | +4.01% |
| PONS/USDT:USDT | below_1h_threshold | +2.43% | +2.45% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.37% | +2.38% |
| 1000BONK/USDT:USDT | below_1h_threshold | +2.05% | +2.07% |
| RAY/USDT:USDT | below_1h_threshold | +1.88% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
