# Decision Report

- generated_at: 2026-08-30T03:31:49.642139+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13003**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13003, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.81% | **+1.97%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.09% | **+1.84%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.00% | **+1.80%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.93% | **+1.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$797.00** / 初期 $100.00 (+697.00%)
- 確定: 4773件 (Win 1457 / Loss 1570 / Flat 1746) / skip 4791件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $797.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.00** / 初期 $100.00 (+74.00%)
- 確定: 2087件 (Win 584 / Loss 506 / Flat 997) / skip 4327件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1331 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $174.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.84** / 初期 $100.00 (+16.84%)
- 確定: 2051件 (Win 604 / Loss 797 / Flat 650) / pending 3件 / skip 2424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000575 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.84

## 6. Latest Market Context

- 更新: 2026-08-30T03:31:38.054498+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=78118.6
- Funnel: target 1023 → liquid 116 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.9 >= 65=1, 4h RSI 85.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +67.30% | $1,768,659.63 |
| PONS/USDT:USDT | +46.03% | $1,423,206.39 |
| FONE/USDT:USDT | +42.22% | $1,288,327.37 |
| HNT/USDT:USDT | +40.24% | $26,975,260.00 |
| PROM/USDT:USDT | +33.23% | $13,552,290.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +4.65% | +4.59% |
| NIULAI/USDT:USDT | below_1h_threshold | +3.57% | +3.51% |
| BLESS/USDT:USDT | below_1h_threshold | +1.41% | +1.35% |
| NEAR/USDT:USDT | below_1h_threshold | +1.13% | +1.07% |
| DEXE/USDT:USDT | below_1h_threshold | +1.12% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
