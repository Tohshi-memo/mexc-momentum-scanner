# Decision Report

- generated_at: 2026-08-26T11:51:30.177161+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12701**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12701, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.16% | **-0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 8/19 | 42.1% | +1.72% | **+0.72%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.69% | **+0.58%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.37% | **+1.23%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.87% | **+1.22%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.12% | **+0.84%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.93% | **+0.51%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.81% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$704.00** / 初期 $100.00 (+604.00%)
- 確定: 4601件 (Win 1400 / Loss 1512 / Flat 1689) / skip 4661件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $704.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$158.72** / 初期 $100.00 (+58.72%)
- 確定: 1996件 (Win 544 / Loss 479 / Flat 973) / skip 4116件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1358 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $158.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.02** / 初期 $100.00 (+17.02%)
- 確定: 1973件 (Win 580 / Loss 751 / Flat 642) / pending 6件 / skip 2195件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000409 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.02

## 6. Latest Market Context

- 更新: 2026-08-26T11:51:21.483004+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=78400.0
- Funnel: target 1023 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.8 >= 65=1, 4h RSI 95.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +255.24% | $16,926,474.45 |
| BMT/USDT:USDT | +53.06% | $15,585,961.96 |
| TAC/USDT:USDT | +52.44% | $7,380,106.10 |
| LONGXIA/USDT:USDT | +27.12% | $1,989,269.38 |
| PONS/USDT:USDT | +21.57% | $1,147,973.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.85% | +3.21% |
| BLESS/USDT:USDT | below_1h_threshold | +1.66% | +2.03% |
| LIGHT/USDT:USDT | below_1h_threshold | +1.27% | +1.64% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.18% | +1.54% |
| STX/USDT:USDT | below_1h_threshold | +1.04% | +1.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
