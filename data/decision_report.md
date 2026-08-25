# Decision Report

- generated_at: 2026-08-25T23:36:21.155457+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12640**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12640, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.22% | **-0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +3.43% | **+1.37%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.88% | **+0.94%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.01% | **+0.61%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.86% | **+0.29%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.96% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.79% | **+2.09%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +2.19% | **+1.75%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +3.03% | **+1.51%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.20% | **+1.43%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.77% | **+1.42%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$687.36** / 初期 $100.00 (+587.36%)
- 確定: 4584件 (Win 1392 / Loss 1506 / Flat 1686) / skip 4617件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BMT/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $687.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1978件 (Win 536 / Loss 473 / Flat 969) / skip 4073件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0553 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$113.86** / 初期 $100.00 (+13.86%)
- 確定: 1934件 (Win 564 / Loss 740 / Flat 630) / pending 0件 / skip 2177件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000114 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.17% 残高後 $113.86

## 6. Latest Market Context

- 更新: 2026-08-25T23:36:11.918257+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=78658.9
- Funnel: target 1023 → liquid 183 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +65.75% | $1,352,622.03 |
| BMT/USDT:USDT | +45.01% | $7,078,943.22 |
| AGI/USDT:USDT | +11.41% | $2,033,203.47 |
| STAR/USDT:USDT | +7.58% | $1,070,604.43 |
| TAC/USDT:USDT | +4.20% | $8,153,509.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGI/USDT:USDT | below_1h_threshold | +2.88% | +3.12% |
| TAC/USDT:USDT | below_1h_threshold | +2.17% | +2.41% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.66% | +0.90% |
| RE/USDT:USDT | below_1h_threshold | +0.60% | +0.84% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +0.50% | +0.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
