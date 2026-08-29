# Decision Report

- generated_at: 2026-08-29T11:51:27.721859+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12934**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12934, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -1.16% | **-0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.59% | **+1.59%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.45% | **+1.16%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.95% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$722.11** / 初期 $100.00 (+622.11%)
- 確定: 4704件 (Win 1424 / Loss 1545 / Flat 1735) / skip 4791件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $722.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$159.84** / 初期 $100.00 (+59.84%)
- 確定: 2018件 (Win 551 / Loss 487 / Flat 980) / skip 4327件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0631 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $159.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.07** / 初期 $100.00 (+16.07%)
- 確定: 2029件 (Win 596 / Loss 787 / Flat 646) / pending 2件 / skip 2372件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000302 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.07

## 6. Latest Market Context

- 更新: 2026-08-29T11:51:13.977324+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=77616.0
- Funnel: target 1023 → liquid 140 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +86.23% | $1,889,084.88 |
| HNT/USDT:USDT | +75.19% | $8,565,570.23 |
| 4/USDT:USDT | +40.38% | $2,443,171.84 |
| LONGXIA/USDT:USDT | +21.48% | $2,114,322.04 |
| O/USDT:USDT | +18.04% | $1,486,517.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +4.92% | +4.91% |
| LONGXIA/USDT:USDT | below_1h_threshold | +3.07% | +3.05% |
| BEAT/USDT:USDT | below_1h_threshold | +2.76% | +2.74% |
| ONG/USDT:USDT | below_1h_threshold | +2.51% | +2.49% |
| DOS/USDT:USDT | below_1h_threshold | +2.09% | +2.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
