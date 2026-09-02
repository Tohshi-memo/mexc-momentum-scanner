# Decision Report

- generated_at: 2026-09-02T02:31:29.011753+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13288**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13288, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.18% | **-2.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 7/20 | 35.0% | +4.44% | **+1.56%** |
| LIMIT_6PCT | 11/20 | 55.0% | +1.39% | **+0.77%** |
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 7/20 | 35.0% | +1.60% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +4.16% | **+3.32%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +3.35% | **+2.85%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +5.51% | **+2.75%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.35% | **+2.23%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +5.10% | **+2.04%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$844.55** / 初期 $100.00 (+744.55%)
- 確定: 4923件 (Win 1501 / Loss 1620 / Flat 1802) / skip 4926件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $844.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.81** / 初期 $100.00 (+75.81%)
- 確定: 2267件 (Win 635 / Loss 545 / Flat 1087) / skip 4432件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1318 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_6PCT` TP_HIT account +0.69% 残高後 $175.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2670件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000408 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-02T02:31:17.470242+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=77224.4
- Funnel: target 1036 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEMI/USDT:USDT | +37.12% | $5,807,377.62 |
| MAGMA/USDT:USDT | +26.49% | $4,947,691.37 |
| UAI/USDT:USDT | +26.13% | $17,841,967.09 |
| FONE/USDT:USDT | +11.26% | $1,381,664.59 |
| CASHCAT/USDT:USDT | +10.76% | $1,164,121.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_relative_strength | +5.15% | +4.83% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.18% | +2.87% |
| ZRO/USDT:USDT | below_1h_threshold | +2.80% | +2.49% |
| BTW/USDT:USDT | below_1h_threshold | +2.56% | +2.25% |
| AR/USDT:USDT | below_1h_threshold | +2.05% | +1.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
