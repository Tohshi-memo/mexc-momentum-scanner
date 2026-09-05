# Decision Report

- generated_at: 2026-09-05T15:46:25.556362+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13745**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13745, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.78% | **-0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.29% | **+0.09%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.09% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.48% | **+1.49%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.67% | **+1.28%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.69% | **+1.19%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.11% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$853.11** / 初期 $100.00 (+753.11%)
- 確定: 5051件 (Win 1519 / Loss 1650 / Flat 1882) / skip 5255件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: USELESS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $853.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.70** / 初期 $100.00 (+89.70%)
- 確定: 2490件 (Win 697 / Loss 587 / Flat 1206) / skip 4666件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0914 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $189.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.33** / 初期 $100.00 (+19.33%)
- 確定: 2369件 (Win 704 / Loss 901 / Flat 764) / pending 3件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000131 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $119.33

## 6. Latest Market Context

- 更新: 2026-09-05T15:46:09.218965+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=79712.3
- Funnel: target 1050 → liquid 133 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +119.72% | $17,989,662.50 |
| 4/USDT:USDT | +68.05% | $22,521,507.01 |
| ICX/USDT:USDT | +41.58% | $1,173,561.69 |
| AKE/USDT:USDT | +39.96% | $20,996,776.31 |
| MARSCOIN/USDT:USDT | +37.53% | $8,607,794.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +3.12% | +3.07% |
| RIVER/USDT:USDT | below_1h_threshold | +2.23% | +2.18% |
| B/USDT:USDT | below_1h_threshold | +1.56% | +1.51% |
| TUT/USDT:USDT | below_1h_threshold | +1.43% | +1.38% |
| DASH/USDT:USDT | below_1h_threshold | +1.26% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
