# Decision Report

- generated_at: 2026-08-20T19:56:37.262762+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12078**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12078, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_7PCT | 6/20 | 30.0% | +3.40% | **+1.02%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_BB3S | 6/11 | 54.5% | +1.14% | **+0.62%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.05% | **+1.54%** |
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +2.10% | **+1.17%** |
| MARKET_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.16% | **+0.75%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.23% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$612.05** / 初期 $100.00 (+512.05%)
- 確定: 4291件 (Win 1312 / Loss 1403 / Flat 1576) / skip 4348件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $612.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3667件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0682 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.73** / 初期 $100.00 (+16.73%)
- 確定: 1771件 (Win 526 / Loss 675 / Flat 570) / pending 5件 / skip 1777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000116 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $116.73

## 6. Latest Market Context

- 更新: 2026-08-20T19:56:21.880478+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=72621.3
- Funnel: target 1011 → liquid 199 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +32.65% | $2,300,154.07 |
| ONG/USDT:USDT | +16.40% | $5,010,518.21 |
| PEOPLE/USDT:USDT | +13.59% | $2,535,610.59 |
| TUT/USDT:USDT | +11.98% | $5,070,106.74 |
| ALLO/USDT:USDT | +9.54% | $4,534,375.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.90% | +3.59% |
| PEOPLE/USDT:USDT | below_1h_threshold | +3.87% | +3.56% |
| TURBO/USDT:USDT | below_1h_threshold | +3.28% | +2.97% |
| HEI/USDT:USDT | below_1h_threshold | +2.51% | +2.21% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.50% | +2.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
