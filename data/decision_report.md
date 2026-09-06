# Decision Report

- generated_at: 2026-09-06T19:36:31.730631+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13828**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.94% / filled 20/20。**
- 全期間 MARKET基準: n=13828, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.94% | **+1.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +2.16% | **+1.94%** |
| MARKET | 20/20 | 100.0% | +1.94% | **+1.94%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.53% | **+1.01%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.76% | **+0.97%** |
| LIMIT_BB3S | 2/19 | 10.5% | +7.37% | **+0.78%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.70% | **+0.26%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| MARKET_LONG | 20/20 | 100.0% | -0.37% | **-0.37%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$837.19** / 初期 $100.00 (+737.19%)
- 確定: 5127件 (Win 1538 / Loss 1680 / Flat 1909) / skip 5262件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $837.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2570件 (Win 717 / Loss 618 / Flat 1235) / skip 4669件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0487 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.64** / 初期 $100.00 (+18.64%)
- 確定: 2437件 (Win 724 / Loss 931 / Flat 782) / pending 6件 / skip 2860件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000114 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.64

## 6. Latest Market Context

- 更新: 2026-09-06T19:36:15.442842+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=79780.1
- Funnel: target 1059 → liquid 126 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +17.18% | $1,131,489.43 |
| MAGMA/USDT:USDT | +14.47% | $2,084,376.22 |
| 4/USDT:USDT | +7.35% | $10,058,613.40 |
| TAO/USDT:USDT | +6.33% | $62,401,661.77 |
| ROSE/USDT:USDT | +5.24% | $1,462,191.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAO/USDT:USDT | below_1h_threshold | +2.60% | +2.76% |
| HEMI/USDT:USDT | below_1h_threshold | +2.36% | +2.53% |
| XAN/USDT:USDT | below_1h_threshold | +1.76% | +1.92% |
| INJ/USDT:USDT | below_1h_threshold | +1.01% | +1.18% |
| SUSHI/USDT:USDT | below_1h_threshold | +1.01% | +1.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
