# Decision Report

- generated_at: 2026-08-25T07:51:43.377953+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12592**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12592, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.97% | **-0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.01% | **+0.41%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.03% | **+0.02%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.13% | **-0.05%** |
| LIMIT_BB3S | 2/16 | 12.5% | -0.82% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.94% | **+1.47%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.19% | **+1.20%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.90% | **+1.14%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.28% | **+1.02%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +3.22% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$712.65** / 初期 $100.00 (+612.65%)
- 確定: 4572件 (Win 1391 / Loss 1497 / Flat 1684) / skip 4581件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $712.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4026件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0745 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.87** / 初期 $100.00 (+15.87%)
- 確定: 1923件 (Win 564 / Loss 730 / Flat 629) / pending 6件 / skip 2137件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000324 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.87

## 6. Latest Market Context

- 更新: 2026-08-25T07:51:25.525349+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.96% price=79777.1
- Funnel: target 1023 → liquid 179 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +80.32% | $4,464,554.39 |
| JIMOTHY/USDT:USDT | +75.63% | $1,051,914.94 |
| TAC/USDT:USDT | +41.13% | $5,149,111.00 |
| CASHCAT/USDT:USDT | +32.17% | $2,949,275.87 |
| ONG/USDT:USDT | +30.05% | $5,185,474.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +3.07% | +4.03% |
| CASHCAT/USDT:USDT | below_1h_threshold | +2.95% | +3.91% |
| RE/USDT:USDT | below_1h_threshold | +2.84% | +3.80% |
| JASMY/USDT:USDT | below_1h_threshold | +2.10% | +3.06% |
| KORU/USDT:USDT | below_1h_threshold | +1.62% | +2.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
