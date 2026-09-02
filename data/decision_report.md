# Decision Report

- generated_at: 2026-09-02T07:56:34.425779+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13320**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13320, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.43% | **-1.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +6.39% | **+1.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_ATR | 8/20 | 40.0% | +2.96% | **+1.18%** |
| LIMIT_BB3S | 9/19 | 47.4% | +2.49% | **+1.18%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.00% | **+1.80%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +5.11% | **+1.79%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.40% | **+1.56%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.85% | **+1.28%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 197件 (TP 73 / SL 119 / EXP 5)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$828.72** / 初期 $100.00 (+728.72%)
- 確定: 4946件 (Win 1503 / Loss 1626 / Flat 1817) / skip 4935件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $828.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$176.32** / 初期 $100.00 (+76.32%)
- 確定: 2299件 (Win 639 / Loss 549 / Flat 1111) / skip 4432件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0351 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BONER/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $176.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 4件 / skip 2701件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000361 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-02T07:56:21.931739+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=77484.1
- Funnel: target 1041 → liquid 158 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 67.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +57.21% | $1,689,166.75 |
| MAGMA/USDT:USDT | +43.33% | $6,608,210.16 |
| CASHCAT/USDT:USDT | +32.66% | $1,603,925.29 |
| BONER/USDT:USDT | +28.75% | $2,633,505.62 |
| UAI/USDT:USDT | +22.97% | $23,637,422.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FF/USDT:USDT | below_1h_threshold | +4.13% | +4.26% |
| FONE/USDT:USDT | below_1h_threshold | +3.85% | +3.97% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.75% | +3.87% |
| CHIP/USDT:USDT | below_1h_threshold | +3.73% | +3.85% |
| USELESS/USDT:USDT | below_1h_threshold | +2.26% | +2.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
