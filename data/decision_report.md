# Decision Report

- generated_at: 2026-09-05T16:56:52.037478+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13755**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13755, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.10% | **-1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.05% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.21% | **+1.33%** |
| MARKET_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.41% | **+1.06%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.93% | **+0.97%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.60% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$852.22** / 初期 $100.00 (+752.22%)
- 確定: 5061件 (Win 1520 / Loss 1652 / Flat 1889) / skip 5255件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $852.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$187.71** / 初期 $100.00 (+87.71%)
- 確定: 2500件 (Win 697 / Loss 590 / Flat 1213) / skip 4666件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0220 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $187.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.22** / 初期 $100.00 (+19.22%)
- 確定: 2378件 (Win 705 / Loss 903 / Flat 770) / pending 6件 / skip 2847件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000201 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.22

## 6. Latest Market Context

- 更新: 2026-09-05T16:56:30.612602+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=80055.5
- Funnel: target 1050 → liquid 133 → pre 50 → checked 50 → surge 7 → strict 2
- Surge前reject: below_1h_threshold=43, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.3 >= 65=1, 4h RSI 76.5 >= 65=1, 4h RSI 69.4 >= 65=1, 4h RSI 68.4 >= 65=1, 4h RSI 72.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +17.07% | $24,297,213.69 |
| USELESS/USDT:USDT | +9.25% | $21,070,076.96 |
| VELVET/USDT:USDT | +8.64% | $1,002,349.45 |
| BASECAT/USDT:USDT | +7.00% | $2,000,202.11 |
| NIULAI/USDT:USDT | +6.13% | $2,116,665.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HNT/USDT:USDT | below_1h_threshold | +4.53% | +4.16% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +4.21% | +3.85% |
| CHIP/USDT:USDT | below_1h_threshold | +3.32% | +2.95% |
| EDGE/USDT:USDT | below_1h_threshold | +3.10% | +2.74% |
| ARB/USDT:USDT | below_1h_threshold | +2.90% | +2.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
